/* ===================================================================
   Th1nk3r Blog — Script
   Theme toggle (dark/light) + mobile menu
   =================================================================== */

(function () {
  'use strict';

  const root = document.documentElement;
  const STORAGE_KEY = 'th1nk3r-theme';

  // --- Theme ---
  function applyTheme(mode) {
    if (mode === 'light') {
      root.classList.add('light');
    } else {
      root.classList.remove('light');
    }
  }

  // Load saved preference or default to dark
  const saved = localStorage.getItem(STORAGE_KEY);
  applyTheme(saved || 'dark');

  document.addEventListener('DOMContentLoaded', function () {
    // Theme toggle buttons (there may be two: desktop + mobile)
    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const isLight = root.classList.contains('light');
        const next = isLight ? 'dark' : 'light';
        applyTheme(next);
        localStorage.setItem(STORAGE_KEY, next);
        // Update icon text
        document.querySelectorAll('.theme-toggle .material-symbols-outlined').forEach(function (icon) {
          icon.textContent = next === 'light' ? 'dark_mode' : 'lightbulb';
        });
      });
    });

    // Set initial icon based on theme
    const currentTheme = root.classList.contains('light') ? 'light' : 'dark';
    document.querySelectorAll('.theme-toggle .material-symbols-outlined').forEach(function (icon) {
      icon.textContent = currentTheme === 'light' ? 'dark_mode' : 'lightbulb';
    });

    // --- Mobile Menu ---
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');

    if (menuBtn && mobileNav) {
      menuBtn.addEventListener('click', function () {
        const isOpen = mobileNav.classList.toggle('open');
        // Swap icon
        const icon = menuBtn.querySelector('.material-symbols-outlined');
        if (icon) icon.textContent = isOpen ? 'close' : 'menu';
      });
    }

    // --- Newsletter Form Validation (OWASP A03: Input Validation) ---
    document.querySelectorAll('.newsletter-form').forEach(function (form) {
      form.addEventListener('submit', function (e) {
        var emailInput = form.querySelector('input[name="email"]');
        if (!emailInput) return;

        var email = emailInput.value.trim();

        // Strict email regex (OWASP recommended pattern)
        var emailPattern = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

        // Sanitize: strip HTML tags to prevent XSS
        var sanitized = email.replace(/<[^>]*>/g, '');

        if (!emailPattern.test(sanitized) || sanitized !== email) {
          e.preventDefault();
          emailInput.setCustomValidity('Please enter a valid email address.');
          emailInput.reportValidity();
          return false;
        }
        emailInput.setCustomValidity('');
      });
    });
  });
})();

