// Code source: Startbootstrap templates

window.addEventListener("DOMContentLoaded", (event) => {
  // Toggle the side navigation
  const sidebarToggle = document.body.querySelector("#sidebarToggle");
  if (sidebarToggle) {
    // Uncomment Below to persist sidebar toggle between refreshes
    // if (localStorage.getItem("sb|sidebar-toggle") === "true") {
    //   document.body.classList.toggle("sb-sidenav-toggled");
    // }
    sidebarToggle.addEventListener("click", (event) => {
      event.preventDefault();
      document.body.classList.toggle("sb-sidenav-toggled");
      localStorage.setItem(
        "sb|sidebar-toggle",
        document.body.classList.contains("sb-sidenav-toggled")
      );
    });
  }
});

// Custom Javascript

// Table click function
document.addEventListener("DOMContentLoaded", function () {
  var clickableRows = document.querySelectorAll(".clickable-row");
  clickableRows.forEach(function (row) {
    row.addEventListener("click", function () {
      var href = row.getAttribute("data-href");
      if (href) {
        window.location.href = href;
      }
    });
  });
});

// Messages timeout function

document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function () {
      const alertElement = document.querySelector(".alert");
      
      if (alertElement) {
          alertElement.remove();
      }
  }, 5000);
});