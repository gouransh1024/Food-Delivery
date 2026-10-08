from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Product, Profile


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='Password123!'
        )
        self.product = Product.objects.create(
            name='Test Pizza',
            price=250.00,
            description='Delicious cheese pizza',
            image='media/default.jpg'
        )

    def test_product_creation(self):
        self.assertEqual(str(self.product), 'Test Pizza')
        self.assertEqual(float(self.product.price), 250.00)

    def test_profile_auto_created_signal(self):
        self.assertTrue(hasattr(self.user, 'profile'))
        self.assertEqual(self.user.profile.user, self.user)


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='johndoe',
            password='SecurePassword123!'
        )
        self.product = Product.objects.create(
            name='Burger',
            price=150.00,
            description='Juicy burger',
            image='media/default.jpg'
        )

    def test_home_page_status(self):
        response = self.client.get(reverse('new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_menu_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertContains(response, 'Burger')

    def test_menu_alias_status(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_status(self):
        response = self.client.get(reverse('loginPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_page_status(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_cart_unauthenticated_redirect(self):
        response = self.client.get(reverse('cart_view'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_cart_authenticated_and_add_item(self):
        self.client.force_login(self.user)
        # Add product to cart
        add_response = self.client.post(reverse('home'), {'product': str(self.product.id)})
        self.assertEqual(add_response.status_code, 302)

        # Add again to test quantity increment
        self.client.post(reverse('home'), {'product': str(self.product.id)})

        # View cart
        cart_response = self.client.get(reverse('cart_view'))
        self.assertEqual(cart_response.status_code, 200)
        self.assertContains(cart_response, 'Burger')
        self.assertContains(cart_response, '300.0')

        # Remove item from cart
        remove_response = self.client.post(reverse('cart_view'), {'remove_product_id': str(self.product.id)})
        self.assertEqual(remove_response.status_code, 302)

    def test_profile_page_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profilePage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_profile_update(self):
        self.client.force_login(self.user)
        update_data = {
            'name': 'John Doe',
            'title': 'Food Enthusiast',
            'desc': 'Loves Italian food'
        }
        response = self.client.post(reverse('profilePage'), update_data)
        self.assertEqual(response.status_code, 302)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.name, 'John Doe')
        self.assertEqual(self.user.profile.title, 'Food Enthusiast')

    def test_user_authentication_flow(self):
        # Test login
        login_response = self.client.post(reverse('loginPage'), {
            'username': 'johndoe',
            'password': 'SecurePassword123!'
        })
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, '/')

        # Test logout
        logout_response = self.client.get(reverse('logOut'))
        self.assertEqual(logout_response.status_code, 302)
        self.assertEqual(logout_response.url, '/login/')
