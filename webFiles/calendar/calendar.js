//TODO: add 'esc' to close event, add 'enter' to open event

//original source: https://www.geeksforgeeks.org/how-to-design-a-simple-calendar-using-javascript/

let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

const day = document.querySelector(".calendar-dates");

const currdate = document
	.querySelector(".calendar-current-date");

const prenexIcons = document
	.querySelectorAll(".calendar-navigation span");

// Array of month names
const months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
];

// Function to generate the calendar
const updatecal = () => {
  
  // Check if the month is out of range
  if (month < 0 || month > 11) {
    // Set the date to the first day of the month with the new year
    date = new Date(year, month, new Date().getDate());

    // Set the year to the new year
    year = date.getFullYear();

    // Set the month to the new month
    month = date.getMonth();
  } else {
    // Set the date to the current date
    date = new Date();
  }
  
  // Get the first day of the month
	let dayone = new Date(year, month, 1).getDay();

	// Get the last date of the month
	let lastdate = new Date(year, month + 1, 0).getDate();

	// Get the day of the last date of the month
	let dayend = new Date(year, month, lastdate).getDay();

	// Get the last date of the previous month
	let monthlastdate = new Date(year, month, 0).getDate();

	// Variable to store the generated calendar HTML
	let lit = "";

	// Loop to add the last dates of the previous month
	for (let i = dayone; i > 0; i--) {
		lit += `<li class="inactive caldate">${monthlastdate - i + 1}</li>`;
	}

	// Loop to add the dates of the current month
	for (let i = 1; i <= lastdate; i++) {

		// Check if the current date is today
		let isToday = i === new Date().getDate()
			&& month === new Date().getMonth()
			&& year === new Date().getFullYear()
			? "active"
			: "";
		lit += `<li class="${isToday} caldate" tabindex="0">${i}</li>`;
	}

	// Loop to add the first dates of the next month
	for (let i = dayend; i < 6; i++) {
		lit += `<li class="inactive caldate">${i - dayend + 1}</li>`;
	}

	// Update the text of the current date element 
	// with the formatted current month and year
  document.getElementById("monthselect").selectedIndex = month;
  document.getElementById("year").value = year;
  
	// update the HTML of the dates element 
	// with the generated calendar
	day.innerHTML = lit;
  updateDateListener();
}

updatecal();

// add event listener to increment icons
prenexIcons.forEach(icon => {
	// When an icon is clicked
	icon.addEventListener("click", incrementmonth);
});

//when one of the buttons is selected
function incrementmonth() {
  // Check if the icon is "calendar-prev"
  // or "calendar-next"
  month = this.id === "calendar-prev" ? month - 1 : month + 1;
  // Call the updatecal function to update the calendar display
  updatecal();  
}


//update when month is changed
document.getElementById("monthselect").addEventListener("change", () => {
  month = parseInt(document.getElementById("monthselect").selectedIndex);
  updatecal();
});

//update when year is changed
document.getElementById("year").addEventListener("change", () => {
  year = parseInt(document.getElementById("year").value);
  updatecal();
});

//when the today button is set, set the month an dyear to the current month and year
document.getElementById("settoday").addEventListener("click", () => {
  month = new Date().getMonth();
  year = new Date().getFullYear();
  updatecal();
});

function updateDateListener() {
  dates = document.getElementsByClassName("caldate");
  for (var i=0;i<dates.length;i++) {
    //only add event lister to current month dates, not the previous or next month
    if(!dates[i].classList.contains("inactive")) {
      dates[i].addEventListener("click",openeventeditor);
    }
  }
}


const eventdiv = document.getElementsByClassName("event-wrap")[0];
function openeventeditor() {
  document.body.addEventListener("mousedown",closeeventeditor);
  eventdiv.style.display = "block";
  if(!isNaN(this.innerText)) {
    d = this.innerText;
    d = (d < 10 ? "0" : "") + d;
  } else {
    d = "01";
  }
  m = parseInt(document.getElementById("monthselect").value)+1;
  m = (m < 10 ? "0" : "") + m;
  y = document.getElementById("year").value;
  document.getElementById("startdate").value = y+"-"+m+"-"+d;
}



function closeeventeditor(e) {
  if(!e.target.closest(".calendar-event") || e.target.classList.contains("closeevent")) {
    shouldclose = confirm("Are you sure you want to cancel your changes?");
    if(shouldclose) {
      document.body.removeEventListener("mousedown",closeeventeditor);
      eventdiv.style.display = "none";
    }
  }
}

function submitevent() {
  console.log("send event");
  document.body.removeEventListener("mousedown",closeeventeditor);
  eventdiv.style.display = "none";
}

document.getElementsByClassName("eventadder")[0].addEventListener("click",openeventeditor);
document.getElementsByClassName("closeevent")[0].addEventListener("click",closeeventeditor);


//TODO: change everything to be tabbable & onkeypress
//TODO: on date select, add an event creator
//TODO: add backend support for saving events
//TODO: load events from backend
//TODO: add different display styles (month, year, week, day)
//TODO: 