// Zabel LLC Directory - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile menu toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');
        });
    }
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Sticky CTA animation
    const stickyCTA = document.querySelector('.sticky-cta');
    if (stickyCTA) {
        // Add entrance animation
        setTimeout(() => {
            stickyCTA.style.opacity = '1';
            stickyCTA.style.transform = 'translateY(0)';
        }, 1000);
    }
    
    // Service comparison expand/collapse
    const serviceItems = document.querySelectorAll('.service-item');
    serviceItems.forEach(item => {
        const header = item.querySelector('.service-header');
        const details = item.querySelector('.service-details');
        
        if (header && details) {
            header.addEventListener('click', function() {
                details.classList.toggle('expanded');
                item.classList.toggle('expanded');
            });
        }
    });
    
    // Form validation for contact form
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic validation
            const name = this.querySelector('input[name="name"]');
            const email = this.querySelector('input[name="email"]');
            
            if (!name.value.trim()) {
                alert('Please enter your name');
                name.focus();
                return;
            }
            
            if (!email.value.trim() || !isValidEmail(email.value)) {
                alert('Please enter a valid email address');
                email.focus();
                return;
            }
            
            // If validation passes, you can submit the form
            // For now, just show a success message
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
    }
    
    // Email validation helper
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // Lazy loading for images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Search functionality (if needed)
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const searchResults = document.querySelectorAll('.searchable-item');
            
            searchResults.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
    
    // Analytics tracking for affiliate links
    const affiliateLinks = document.querySelectorAll('a[href*="consumer-champion.org"]');
    affiliateLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Track affiliate link clicks
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    'event_category': 'affiliate',
                    'event_label': this.href
                });
            }
        });
    });
    
    // Back to top button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '↑';
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.style.cssText = `
        position: fixed;
        bottom: 80px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #f39c12;
        color: white;
        border: none;
        cursor: pointer;
        font-size: 20px;
        opacity: 0;
        transition: opacity 0.3s;
        z-index: 999;
    `;
    
    document.body.appendChild(backToTopBtn);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.opacity = '1';
        } else {
            backToTopBtn.style.opacity = '0';
        }
    });
    
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Performance optimization: Debounce scroll events
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Apply debouncing to scroll events
    const debouncedScrollHandler = debounce(function() {
        // Handle scroll events here if needed
    }, 100);
    
    window.addEventListener('scroll', debouncedScrollHandler);
    
    console.log('Zabel LLC Directory - JavaScript loaded successfully');
});
