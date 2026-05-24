(() => {
  const root = document.documentElement;
  const key = "rimreck-theme";
  const toggle = document.getElementById("theme-toggle");
  const current = localStorage.getItem(key);
  if (current) {
    root.setAttribute("data-theme", current);
  }
  if (toggle) {
    toggle.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem(key, next);
    });
  }
})();
