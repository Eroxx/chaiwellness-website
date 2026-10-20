// One place for contact details. Switch to hello@<domain> once the domain's Email Routing is set up.
var CONTACT_EMAIL = "eric.linder@gmail.com";

(function () {
  var form = document.getElementById("contact");
  if (!CONTACT_EMAIL) return;
  var direct = document.getElementById("direct");
  if (direct) {
    var a = document.getElementById("direct-link");
    a.href = "mailto:" + CONTACT_EMAIL; a.textContent = CONTACT_EMAIL; direct.hidden = false;
  }
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var status = document.getElementById("status");
    var f = new FormData(form);
    var name = (f.get("name") || "").trim(), email = (f.get("email") || "").trim(), msg = (f.get("message") || "").trim();
    if (!name || !email || !msg) { status.style.color = ""; status.textContent = "Please add your name, email and a short message."; return; }
    var body = msg + "\n\n" + name + (f.get("org") ? "\n" + f.get("org") : "") + "\n" + email;
    var subject = "Chai Wellness: " + f.get("topic");
    window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    status.textContent = "Your email app should open with the message ready to send.";
  });
})();
