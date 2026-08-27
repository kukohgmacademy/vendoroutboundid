/* Vendor Outbound — script.js
   JS minimal, hanya untuk interaksi navigasi.
   Semua konten inti sudah tersedia di HTML tanpa bergantung pada JS ini. */

(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  var toggle = header && header.querySelector(".menu-toggle");
  var menu = header && header.querySelector(".nav-menu");

  // --- Mobile menu toggle ---
  if (toggle && menu) {
    toggle.addEventListener("click", function (e) {
      e.stopPropagation();
      var isOpen = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });

    // Close when clicking outside menu on mobile
    document.addEventListener("click", function (e) {
      if (menu.classList.contains("is-open") && !menu.contains(e.target) && !toggle.contains(e.target)) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });

    // Close with Escape key
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });
  }

  // --- Mega menu (Paket) toggle: klik & keyboard ---
  var megaTriggers = document.querySelectorAll("[data-mega-trigger]");
  megaTriggers.forEach(function (trigger) {
    var panel = document.getElementById(trigger.getAttribute("aria-controls"));
    if (!panel) return;

    function closePanel() {
      panel.classList.remove("is-open");
      trigger.setAttribute("aria-expanded", "false");
    }
    function openPanel() {
      panel.classList.add("is-open");
      trigger.setAttribute("aria-expanded", "true");
    }

    trigger.addEventListener("click", function (e) {
      // Hanya jadikan tombol toggle pada layar sempit (mobile),
      // di desktop mega menu sudah muncul lewat :hover/:focus-within di CSS.
      if (window.matchMedia("(max-width: 768px)").matches) {
        e.preventDefault();
        e.stopPropagation();
        var isOpen = panel.classList.contains("is-open");
        isOpen ? closePanel() : openPanel();
      }
    });

    trigger.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closePanel();
    });
  });

  // Tutup menu mobile saat pindah ke layar lebar
  window.addEventListener("resize", function () {
    if (window.innerWidth > 768 && menu && menu.classList.contains("is-open")) {
      menu.classList.remove("is-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    }
  });

  // Tutup menu mobile saat sebuah link diklik
  if (menu) {
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 768px)").matches && !link.hasAttribute("data-mega-trigger")) {
          menu.classList.remove("is-open");
          if (toggle) toggle.setAttribute("aria-expanded", "false");
          document.body.style.overflow = "";
        }
      });
    });
  }

  // --- Scroll Reveal Animation System (Smooth & Modern) ---
  function initScrollReveal() {
    // Cek preferensi aksesibilitas pengguna (reduced motion)
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      return;
    }

    // Aktifkan mode reveal pada document
    document.documentElement.classList.add("reveal-ready");

    var selectorList = [
      // Hero & header elements
      ".hero-copy",
      ".hero-media",
      ".hero-stats-row > .stat-box",

      // Grids & cards
      ".tall-cards-row > .tall-card",
      ".programs-grid > .program-card",
      ".gallery-bento > .gallery-bento-item",
      ".initiative-cards-row > .initiative-card",
      ".consultation-box",
      ".grid > .card",
      ".grid > *",
      ".faq-help-card",
      ".faq-stack > .faq-card",
      ".faq-list > .faq-item",
      ".mission-copy",
      ".trust-strip",

      // Content blocks & sections
      ".programs-header-wrap",
      ".gallery-header-wrap",
      ".blog-section-header",
      ".featured-blog-grid > .featured-blog-card",
      ".testi-grid > .testi-card",
      "section > .container > .eyebrow",
      "section > .container > h1",
      "section > .container > h2",
      "section > .container > .lead",
      ".answer-box",
      ".info-table",
      ".price-note",
      ".cta-band",
      ".cta-banner",
      ".contact-card",
      ".contact-form",
      ".footer-grid > *",

      // Manual reveal attribute
      "[data-reveal]",
      ".reveal"
    ];

    var candidateElements = document.querySelectorAll(selectorList.join(", "));
    var revealItems = [];

    candidateElements.forEach(function (el) {
      // Kecualikan navigasi/header, breadcrumb, marquee track, dan script/tags tersembunyi
      if (el.closest(".site-header") || el.closest(".breadcrumb") || el.closest(".nav-menu") || el.closest(".trust-marquee-wrapper")) {
        return;
      }
      if (revealItems.indexOf(el) === -1) {
        revealItems.push(el);
      }
    });

    if (revealItems.length === 0) return;

    revealItems.forEach(function (el) {
      el.classList.add("reveal-item");

      // Custom direction jika diset via data-reveal
      var direction = el.getAttribute("data-reveal");
      if (direction) {
        el.classList.add("reveal-" + direction);
      }

      // Auto-stagger delay untuk item dalam container grid / deretan kartu
      var parent = el.parentElement;
      if (parent && (
        parent.classList.contains("grid") ||
        parent.classList.contains("gallery-grid") ||
        parent.classList.contains("gallery-bento") ||
        parent.classList.contains("tall-cards-row") ||
        parent.classList.contains("programs-grid") ||
        parent.classList.contains("initiative-cards-row") ||
        parent.classList.contains("hero-stats-row") ||
        parent.classList.contains("faq-list") ||
        parent.classList.contains("trust-logos") ||
        parent.classList.contains("footer-grid")
      )) {
        var index = Array.prototype.indexOf.call(parent.children, el);
        if (index >= 0) {
          var delay = Math.min(index * 0.08, 0.5);
          if (delay > 0) {
            el.style.transitionDelay = delay + "s";
          }
        }
      }
    });

    function revealElement(el) {
      el.classList.add("is-revealed");
      // Bersihkan transitionDelay setelah selesai agar interaksi hover instan
      setTimeout(function () {
        el.style.transitionDelay = "";
      }, 900);
    }

    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(
        function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              revealElement(entry.target);
              obs.unobserve(entry.target);
            }
          });
        },
        {
          root: null,
          rootMargin: "0px 0px -40px 0px",
          threshold: 0.08
        }
      );

      revealItems.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        // Jika elemen sudah berada dalam viewport pada initial load, langsung tampilkan
        if (rect.top < window.innerHeight - 30) {
          revealElement(el);
        } else {
          observer.observe(el);
        }
      });
    } else {
      // Fallback untuk browser lawas
      revealItems.forEach(function (el) {
        revealElement(el);
      });
    }
  }

  // --- Floating Back to Top Button ---
  function initBackToTop() {
    var btn = document.getElementById("backToTop");
    if (!btn) {
      btn = document.createElement("button");
      btn.id = "backToTop";
      btn.className = "back-to-top";
      btn.setAttribute("type", "button");
      btn.setAttribute("aria-label", "Kembali ke atas");
      btn.setAttribute("title", "Kembali ke atas");
      btn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>';
      document.body.appendChild(btn);
    }

    var ticking = false;
    function updateBackToTop() {
      if (window.pageYOffset > 280) {
        btn.classList.add("is-visible");
      } else {
        btn.classList.remove("is-visible");
      }
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(updateBackToTop);
        ticking = true;
      }
    }, { passive: true });

    updateBackToTop();

    btn.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  function initWhatsAppFloatIcon() {
    var waFloats = document.querySelectorAll(".wa-float");
    waFloats.forEach(function (el) {
      el.innerHTML = '<span class="wa-badge">!</span><span class="wa-tooltip">Hubungi +62 822-1122-1909</span><svg viewBox="0 0 32 32" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M16 3C8.82 3 3 8.82 3 16c0 2.45.68 4.75 1.88 6.72L3.5 28.5l6.02-1.34A12.92 12.92 0 0016 29c7.18 0 13-5.82 13-13S23.18 3 16 3zm0 2.4c5.85 0 10.6 4.75 10.6 10.6 0 5.85-4.75 10.6-10.6 10.6-2.02 0-3.92-.57-5.54-1.56l-.4-.24-3.92.87.89-3.78-.26-.42A10.53 10.53 0 015.4 16C5.4 10.15 10.15 5.4 16 5.4zm5.95 13.78c-.26-.13-1.55-.77-1.79-.86-.24-.09-.42-.13-.59.13-.17.26-.68.86-.83 1.03-.15.17-.31.2-.57.07-.26-.13-1.1-.41-2.1-1.3-.78-.69-1.3-1.55-1.45-1.81-.15-.26-.02-.4.11-.53.12-.12.26-.31.39-.46.13-.15.17-.26.26-.44.09-.17.04-.33-.02-.46-.07-.13-.59-1.42-.81-1.95-.21-.51-.43-.44-.59-.45h-.51c-.17 0-.46.07-.7.33-.24.26-.92.9-.92 2.2 0 1.3.94 2.55 1.07 2.73.13.17 1.86 2.84 4.51 3.98.63.27 1.12.44 1.51.56.63.2 1.21.17 1.67.1.51-.08 1.55-.63 1.77-1.25.22-.61.22-1.14.15-1.25-.07-.11-.24-.17-.5-.3z"/></svg>';
    });
  }

  function initWhatsAppCTAButtons() {
    var ctaButtons = document.querySelectorAll(".btn-wa:not(.wa-float)");
    ctaButtons.forEach(function (btn) {
      // Sinkronkan ikon SVG agar 100% sama persis dengan floating WA
      var svg = btn.querySelector("svg");
      if (svg) {
        svg.setAttribute("viewBox", "0 0 32 32");
        svg.innerHTML = '<path fill-rule="evenodd" clip-rule="evenodd" d="M16 3C8.82 3 3 8.82 3 16c0 2.45.68 4.75 1.88 6.72L3.5 28.5l6.02-1.34A12.92 12.92 0 0016 29c7.18 0 13-5.82 13-13S23.18 3 16 3zm0 2.4c5.85 0 10.6 4.75 10.6 10.6 0 5.85-4.75 10.6-10.6 10.6-2.02 0-3.92-.57-5.54-1.56l-.4-.24-3.92.87.89-3.78-.26-.42A10.53 10.53 0 015.4 16C5.4 10.15 10.15 5.4 16 5.4zm5.95 13.78c-.26-.13-1.55-.77-1.79-.86-.24-.09-.42-.13-.59.13-.17.26-.68.86-.83 1.03-.15.17-.31.2-.57.07-.26-.13-1.1-.41-2.1-1.3-.78-.69-1.3-1.55-1.45-1.81-.15-.26-.02-.4.11-.53.12-.12.26-.31.39-.46.13-.15.17-.26.26-.44.09-.17.04-.33-.02-.46-.07-.13-.59-1.42-.81-1.95-.21-.51-.43-.44-.59-.45h-.51c-.17 0-.46.07-.7.33-.24.26-.92.9-.92 2.2 0 1.3.94 2.55 1.07 2.73.13.17 1.86 2.84 4.51 3.98.63.27 1.12.44 1.51.56.63.2 1.21.17 1.67.1.51-.08 1.55-.63 1.77-1.25.22-.61.22-1.14.15-1.25-.07-.11-.24-.17-.5-.3z"/>';
      }

      if (!btn.querySelector(".btn-wa-badge")) {
        var badge = document.createElement("span");
        badge.className = "btn-wa-badge";
        badge.textContent = "!";
        badge.setAttribute("aria-hidden", "true");
        btn.appendChild(badge);
      }
    });
  }

  function initHeaderScroll() {
    var siteHeader = document.querySelector(".site-header");
    if (!siteHeader) return;

    var ticking = false;
    function checkScroll() {
      if (window.pageYOffset > 25) {
        siteHeader.classList.add("is-scrolled");
      } else {
        siteHeader.classList.remove("is-scrolled");
      }
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(checkScroll);
        ticking = true;
      }
    }, { passive: true });

    checkScroll();
  }

  function initWanderWidgets() {
    var tabs = document.querySelectorAll(".wander-tab");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          t.classList.remove("active");
          t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("active");
        tab.setAttribute("aria-selected", "true");

        var tabType = tab.getAttribute("data-tab");
        var submitBtn = document.querySelector(".wander-card-submit span");
        if (submitBtn) {
          if (tabType === "perusahaan") submitBtn.textContent = "Cari Paket Perusahaan";
          else if (tabType === "gathering") submitBtn.textContent = "Cari Paket Gathering";
          else if (tabType === "sekolah") submitBtn.textContent = "Cari Paket Sekolah";
          else if (tabType === "wisata" || tabType === "adventure") submitBtn.textContent = "Cari Paket Wisata";
          else submitBtn.textContent = "Cari & Konsultasi Paket";
        }
      });
    });
  }

  // Global helper functions
  window.setDestinationArea = function (areaName, btnElement) {
    var toInput = document.getElementById("searchToInput");
    if (toInput) {
      toInput.value = areaName;
      toInput.focus();
    }
    if (btnElement) {
      var chips = document.querySelectorAll(".area-chip");
      chips.forEach(function (c) { c.classList.remove("active"); });
      btnElement.classList.add("active");
    }
  };

  window.swapLocations = function () {
    var fromInput = document.getElementById("searchFromInput");
    var toInput = document.getElementById("searchToInput");
    if (fromInput && toInput) {
      var temp = fromInput.value;
      fromInput.value = toInput.value;
      toInput.value = temp;
    }
  };

  window.scrollDestinations = function (direction) {
    var container = document.getElementById("wanderDestCards");
    if (container) {
      var scrollAmount = 260 * direction;
      container.scrollBy({ left: scrollAmount, behavior: "smooth" });
    }
  };

  window.handleWanderSearch = function (e) {
    e.preventDefault();
    var activeTab = document.querySelector(".wander-tab.active");
    var category = activeTab ? activeTab.querySelector("span").textContent.trim() : "Trip";
    var fromVal = document.getElementById("searchFromInput") ? document.getElementById("searchFromInput").value : "";
    var toVal = document.getElementById("searchToInput") ? document.getElementById("searchToInput").value : "";
    var datesVal = document.getElementById("searchDatesInput") ? document.getElementById("searchDatesInput").value : "";
    var travelersVal = document.getElementById("searchTravelersInput") ? document.getElementById("searchTravelersInput").value : "";

    var text = "Halo Vendor Outbound, saya ingin konsultasi rencana kegiatan:\n" +
      "• Kategori: " + category + "\n" +
      "• Dari: " + fromVal + "\n" +
      "• Ke / Tujuan: " + toVal + "\n" +
      "• Tanggal: " + datesVal + "\n" +
      "• Peserta / Travelers: " + travelersVal;

    var waUrl = "https://wa.me/6282211221909?text=" + encodeURIComponent(text);
    window.open(waUrl, "_blank", "noopener");
  };

  // ==========================================
  // ELEGANT GALLERY LIGHTBOX PREVIEW SYSTEM
  // ==========================================
  function initGalleryLightbox() {
    var lightbox = document.getElementById("galleryLightbox");
    var galleryItems = document.querySelectorAll("[data-gallery-item]");
    if (!lightbox || !galleryItems.length) return;

    var mainImg = document.getElementById("lightboxMainImg");
    var tagEl = document.getElementById("lightboxTag");
    var counterEl = document.getElementById("lightboxCounter");
    var locationEl = document.getElementById("lightboxLocationText");
    var titleEl = document.getElementById("lightboxTitle");
    var prevBtn = document.getElementById("lightboxPrevBtn");
    var nextBtn = document.getElementById("lightboxNextBtn");
    var closeBtn = document.getElementById("lightboxCloseBtn");
    var zoomBtn = document.getElementById("lightboxZoomToggle");
    var thumbsContainer = document.getElementById("lightboxThumbs");
    var backdrop = document.getElementById("lightboxBackdrop");

    var currentIndex = 0;
    var isZoomed = false;
    var touchStartX = 0;
    var touchStartY = 0;

    // Collect data from DOM
    var itemsData = [];
    galleryItems.forEach(function (el, idx) {
      var img = el.querySelector("img");
      var tag = el.getAttribute("data-tag") || (el.querySelector(".gallery-tag-pill") ? el.querySelector(".gallery-tag-pill").textContent.trim() : "");
      var title = el.getAttribute("data-title") || (el.querySelector(".gallery-title") ? el.querySelector(".gallery-title").textContent.trim() : "");
      var location = el.getAttribute("data-location") || (el.querySelector(".gallery-location span") ? el.querySelector(".gallery-location span").textContent.trim() : "");
      var src = el.getAttribute("data-src") || (img ? img.getAttribute("src") : "");
      var alt = (img ? img.getAttribute("alt") : "") || title;

      itemsData.push({
        src: src,
        alt: alt,
        tag: tag,
        title: title,
        location: location
      });

      // Attach trigger to each gallery card
      el.addEventListener("click", function (e) {
        e.preventDefault();
        openLightbox(idx);
      });

      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openLightbox(idx);
        }
      });
    });

    // Build Thumbnail Navigation Strip
    if (thumbsContainer) {
      thumbsContainer.innerHTML = "";
      itemsData.forEach(function (data, idx) {
        var thumbBtn = document.createElement("button");
        thumbBtn.type = "button";
        thumbBtn.className = "lightbox-thumb-btn" + (idx === 0 ? " is-active" : "");
        thumbBtn.setAttribute("aria-label", "Lihat foto ke-" + (idx + 1) + ": " + data.title);
        thumbBtn.innerHTML = '<img src="' + data.src + '" alt="' + data.alt + '" loading="lazy">';
        
        thumbBtn.addEventListener("click", function () {
          goToSlide(idx);
        });
        thumbsContainer.appendChild(thumbBtn);
      });
    }

    function setZoomState(zoomed) {
      isZoomed = zoomed;
      if (mainImg) {
        if (isZoomed) {
          mainImg.classList.add("is-zoomed");
        } else {
          mainImg.classList.remove("is-zoomed");
        }
      }
      if (zoomBtn) {
        var zoomInIcon = zoomBtn.querySelector(".icon-zoom-in");
        var zoomOutIcon = zoomBtn.querySelector(".icon-zoom-out");
        if (zoomInIcon && zoomOutIcon) {
          zoomInIcon.style.display = isZoomed ? "none" : "";
          zoomOutIcon.style.display = isZoomed ? "" : "none";
        }
        zoomBtn.setAttribute("title", isZoomed ? "Perkecil (Klik 2x / Esc)" : "Perbesar (Klik 2x pada foto)");
      }
    }

    function renderSlide(index, animate) {
      if (index < 0 || index >= itemsData.length) return;
      currentIndex = index;
      setZoomState(false);

      var data = itemsData[currentIndex];

      if (tagEl) tagEl.textContent = data.tag;
      if (counterEl) counterEl.textContent = (currentIndex + 1) + " / " + itemsData.length;
      if (locationEl) locationEl.textContent = data.location;
      if (titleEl) titleEl.textContent = data.title;

      if (mainImg) {
        if (animate) {
          mainImg.classList.add("is-animating");
          setTimeout(function () {
            mainImg.src = data.src;
            mainImg.alt = data.alt;
            mainImg.onload = function () {
              mainImg.classList.remove("is-animating");
            };
            // Fallback jika sudah di-cache
            if (mainImg.complete) {
              mainImg.classList.remove("is-animating");
            }
          }, 150);
        } else {
          mainImg.src = data.src;
          mainImg.alt = data.alt;
        }
      }

      // Update thumbnails active state
      if (thumbsContainer) {
        var thumbBtns = thumbsContainer.querySelectorAll(".lightbox-thumb-btn");
        thumbBtns.forEach(function (btn, idx) {
          if (idx === currentIndex) {
            btn.classList.add("is-active");
            btn.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
          } else {
            btn.classList.remove("is-active");
          }
        });
      }

      // Preload next & previous images for lightning fast response
      var nextIdx = (currentIndex + 1) % itemsData.length;
      var prevIdx = (currentIndex - 1 + itemsData.length) % itemsData.length;
      new Image().src = itemsData[nextIdx].src;
      new Image().src = itemsData[prevIdx].src;
    }

    function openLightbox(index) {
      renderSlide(index, false);
      lightbox.classList.add("is-open");
      lightbox.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";

      // Focus close button for accessibility
      if (closeBtn) closeBtn.focus();
    }

    function closeLightbox() {
      lightbox.classList.remove("is-open");
      lightbox.setAttribute("aria-hidden", "true");
      setZoomState(false);
      document.body.style.overflow = "";

      // Return focus to active trigger
      if (galleryItems[currentIndex]) {
        galleryItems[currentIndex].focus();
      }
    }

    function nextSlide() {
      var nextIdx = (currentIndex + 1) % itemsData.length;
      renderSlide(nextIdx, true);
    }

    function prevSlide() {
      var prevIdx = (currentIndex - 1 + itemsData.length) % itemsData.length;
      renderSlide(prevIdx, true);
    }

    function goToSlide(index) {
      if (index !== currentIndex) {
        renderSlide(index, true);
      }
    }

    // Event Listeners
    if (prevBtn) {
      prevBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        prevSlide();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        nextSlide();
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        closeLightbox();
      });
    }

    if (backdrop) {
      backdrop.addEventListener("click", function () {
        closeLightbox();
      });
    }

    if (zoomBtn) {
      zoomBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        setZoomState(!isZoomed);
      });
    }

    if (mainImg) {
      mainImg.addEventListener("dblclick", function (e) {
        e.preventDefault();
        setZoomState(!isZoomed);
      });
    }

    // Keyboard Shortcuts
    document.addEventListener("keydown", function (e) {
      if (!lightbox.classList.contains("is-open")) return;

      if (e.key === "Escape") {
        if (isZoomed) {
          setZoomState(false);
        } else {
          closeLightbox();
        }
      } else if (e.key === "ArrowRight") {
        nextSlide();
      } else if (e.key === "ArrowLeft") {
        prevSlide();
      }
    });

    // Touch Swipe Gesture for Mobile
    lightbox.addEventListener("touchstart", function (e) {
      if (e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }
    }, { passive: true });

    lightbox.addEventListener("touchend", function (e) {
      if (isZoomed) return; // Disable swipe when zoomed
      if (e.changedTouches.length === 1) {
        var diffX = e.changedTouches[0].clientX - touchStartX;
        var diffY = e.changedTouches[0].clientY - touchStartY;
        // Check horizontal swipe threshold (min 45px) and ensure horizontal intent
        if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.5) {
          if (diffX < 0) {
            nextSlide(); // Swipe Left -> Next
          } else {
            prevSlide(); // Swipe Right -> Prev
          }
        }
      }
    }, { passive: true });
  }

  // ==========================================
  // INTERACTIVE TESTIMONIALS SYSTEM
  // ==========================================
  function initTestimonials() {
    var cards = document.querySelectorAll(".testi-grid .testi-card");
    if (!cards.length) return;

    cards.forEach(function (card) {
      card.addEventListener("click", function () {
        cards.forEach(function (c) {
          c.classList.remove("testi-card-featured");
        });
        card.classList.add("testi-card-featured");
      });
    });
  }


  function initApp() {
    initHeaderScroll();
    initScrollReveal();
    initBackToTop();
    initWhatsAppFloatIcon();
    initWhatsAppCTAButtons();
    initWanderWidgets();
    initGalleryLightbox();
    initTestimonials();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initApp);
  } else {
    initApp();
  }
})();
