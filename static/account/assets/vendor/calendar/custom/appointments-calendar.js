
document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("appointmentsCal");
  var calendar = new FullCalendar.Calendar(calendarEl, {
    headerToolbar: {
      left: "prevYear,prev,next,nextYear today",
      center: "title",
      right: "dayGridMonth,dayGridWeek,dayGridDay",
    },
    initialView: "dayGridMonth",  // Initial view of the calendar
    events: "appointments-json/",  // URL to fetch JSON events data
    editable: true,
    dayMaxEvents: true,
  });

  calendar.render();  // Render the calendar
});

