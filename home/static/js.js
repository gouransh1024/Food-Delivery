const hamburger = document.querySelector(".hamburger");
const closeBtn = document.querySelector(".nav-list .close");
const navMenu = document.querySelector(".nav-list");

if (hamburger && navMenu) {
    hamburger.addEventListener("click", () => {
        navMenu.classList.add("show");
    });
}

if (closeBtn && navMenu) {
    closeBtn.addEventListener("click", () => {
        navMenu.classList.remove("show");
    });
}

// <!--=============== SignIn Form ===============-->
const signInModal = document.querySelector(".header .wrapper");
const signInBtn = document.querySelector(".sign-in");
const closeFormBtn = document.querySelector(".close-form");

if (signInBtn && signInModal && signInBtn.tagName.toLowerCase() !== 'a') {
    signInBtn.onclick = (e) => {
        e.preventDefault();
        signInModal.classList.add("active");
    };
}

if (closeFormBtn && signInModal) {
    closeFormBtn.onclick = () => {
        signInModal.classList.remove("active");
    };
}