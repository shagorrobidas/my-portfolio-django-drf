(function() {
    function initPasswordToggle() {
        const passwordInput = document.getElementById('id_password');
        // Prevent duplicate initialization
        if (passwordInput && !passwordInput.dataset.toggleInitialized) {
            passwordInput.dataset.toggleInitialized = "true";

            // 1. Create a relative container wrapper
            const wrapper = document.createElement('div');
            wrapper.className = 'relative w-full';

            // 2. Insert wrapper before input, and move input into wrapper
            passwordInput.parentNode.insertBefore(wrapper, passwordInput);
            wrapper.appendChild(passwordInput);

            // 3. Adjust passwordInput padding on the right to make space for the icon
            passwordInput.style.paddingRight = '44px';

            // 4. Create toggle button
            const toggleBtn = document.createElement('button');
            toggleBtn.type = 'button';
            toggleBtn.className = 'absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:text-gray-500 dark:hover:text-gray-300 cursor-pointer flex items-center justify-center';
            toggleBtn.style.border = 'none';
            toggleBtn.style.background = 'none';
            toggleBtn.style.padding = '0';
            toggleBtn.style.outline = 'none';

            // Use Unfold's Material Symbols font
            const icon = document.createElement('span');
            icon.className = 'material-symbols-outlined';
            icon.style.fontSize = '20px';
            icon.textContent = 'visibility';
            toggleBtn.appendChild(icon);

            wrapper.appendChild(toggleBtn);

            // 5. Add event listener
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                if (passwordInput.type === 'password') {
                    passwordInput.type = 'text';
                    icon.textContent = 'visibility_off';
                } else {
                    passwordInput.type = 'password';
                    icon.textContent = 'visibility';
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initPasswordToggle);
    } else {
        initPasswordToggle();
    }
})();
