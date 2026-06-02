(function () {
  const adsClient = "ca-pub-6428701926694635";
  const analyticsId = "G-CLJNJ2GEVB";
  const loadDelayMs = 3000;
  let loaded = false;
  let timer = null;

  function loadScript(src, attributes) {
    if (document.querySelector(`script[src="${src}"]`)) return;
    const script = document.createElement("script");
    script.async = true;
    script.src = src;
    Object.entries(attributes || {}).forEach(([key, value]) => {
      script[key] = value;
    });
    document.head.appendChild(script);
  }

  function loadThirdParty() {
    if (loaded) return;
    loaded = true;
    if (timer) window.clearTimeout(timer);

    loadScript(
      `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${adsClient}`,
      { crossOrigin: "anonymous" }
    );

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {
      window.dataLayer.push(arguments);
    };
    window.gtag("js", new Date());
    window.gtag("config", analyticsId);
    loadScript(`https://www.googletagmanager.com/gtag/js?id=${analyticsId}`);
  }

  function scheduleLoad() {
    timer = window.setTimeout(loadThirdParty, loadDelayMs);
    ["pointerdown", "keydown", "scroll", "touchstart"].forEach((eventName) => {
      window.addEventListener(eventName, loadThirdParty, { once: true, passive: true });
    });
  }

  if (document.readyState === "complete") {
    scheduleLoad();
  } else {
    window.addEventListener("load", scheduleLoad, { once: true });
  }
})();
