(() => {
  "use strict";

  const button = document.querySelector("#copy-example");
  const message = document.querySelector("#copy-message");
  if (!button || !message) return;

  const snippet = `<link rel="stylesheet" href="css/unhinged.css">\n<section class="ud-card">\n  <p class="ud-label">Signal / 01</p>\n  <h2 class="ud-heading ud-heading--brand">Make it glow</h2>\n</section>`;

  const announce = (text) => {
    message.textContent = text;
    window.setTimeout(() => {
      if (message.textContent === text) message.textContent = "";
    }, 3500);
  };

  const fallbackCopy = () => {
    const helper = document.createElement("textarea");
    helper.value = snippet;
    helper.setAttribute("readonly", "");
    helper.style.position = "fixed";
    helper.style.opacity = "0";
    document.body.appendChild(helper);
    helper.select();
    let copied = false;
    try {
      copied = document.execCommand("copy");
    } catch (_error) {
      copied = false;
    }
    helper.remove();
    return copied;
  };

  button.addEventListener("click", async () => {
    let copied = false;
    if (navigator.clipboard && window.isSecureContext) {
      try {
        await navigator.clipboard.writeText(snippet);
        copied = true;
      } catch (_error) {
        copied = false;
      }
    }
    if (!copied) copied = fallbackCopy();
    announce(copied ? "Starter markup copied." : "Copy is unavailable here; select the example in the README.");
  });
})();
