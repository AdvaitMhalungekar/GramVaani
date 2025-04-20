// script.js - Updated for navbar integration

// Function to initialize Google Translate
function googleTranslateElementInit() {
    new google.translate.TranslateElement(
      {pageLanguage: 'en'},
      'google_translate_element'
    );
    
    // Add listener for translation changes
    if (window.addEventListener) {
      document.addEventListener('gtranslate', saveLanguagePreference, false);
    }
  }
  
  // Function to save the selected language to localStorage
  function saveLanguagePreference() {
    setTimeout(function() {
      const langSelect = document.querySelector('.goog-te-combo');
      if (langSelect) {
        const selectedLanguage = langSelect.value;
        localStorage.setItem('preferred_language', selectedLanguage);
      }
    }, 1000);
  }
  
  // Function to apply the saved language preference on page load
  function loadLanguagePreference() {
    const savedLanguage = localStorage.getItem('preferred_language');
    if (savedLanguage && savedLanguage !== 'select language') {
      setTimeout(function() {
        const langSelect = document.querySelector('.goog-te-combo');
        if (langSelect) {
          langSelect.value = savedLanguage;
          // Trigger change event
          const event = new Event('change');
          langSelect.dispatchEvent(event);
        }
      }, 1000);
    }
  }
  
  // Run when the page loads
  document.addEventListener('DOMContentLoaded', function() {
    // Load Google Translate script if not already loaded
    if (!window.google || !window.google.translate) {
      const translateScript = document.createElement('script');
      translateScript.type = 'text/javascript';
      translateScript.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
      document.body.appendChild(translateScript);
      
      translateScript.onload = function() {
        loadLanguagePreference();
      };
    } else {
      // Google Translate already loaded
      loadLanguagePreference();
    }
    
    // Create custom event to detect translation changes
    const originalChange = HTMLSelectElement.prototype.dispatchEvent;
    HTMLSelectElement.prototype.dispatchEvent = function(event) {
      if (this.classList.contains('goog-te-combo') && event.type === 'change') {
        document.dispatchEvent(new Event('gtranslate'));
      }
      return originalChange.apply(this, arguments);
    };
  });
  
  // Additional event listener for the mic button if needed
  document.addEventListener('DOMContentLoaded', function() {
    const micButton = document.querySelector('.mic-navbar');
    if (micButton) {
      micButton.addEventListener('click', function() {
        // Your microphone functionality here
      });
    }
  });