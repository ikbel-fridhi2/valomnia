// // document.addEventListener("DOMContentLoaded", function() {
// //     // Get both forms
// //     let employeeForm = document.getElementById("employeeForm");
// //     let employeeDateForm = document.getElementById("employeeDateForm");

// //     // Add event listener to handle both form submissions
// //     employeeForm.addEventListener("submit", function(event) {
// //         event.preventDefault();
// //         handleFormSubmission(employeeForm, "dates-result");
// //     });

// //     employeeDateForm.addEventListener("submit", function(event) {
// //         event.preventDefault();
// //         handleFormSubmission(employeeDateForm, "data-result");
// //     });

// //     function handleFormSubmission(form, resultDivId) {
// //         fetch(form.getAttribute("action"), {
// //             method: "POST",
// //             body: new FormData(form),
// //         })
// //         .then(response => response.json())
// //         .then(data => {
// //             // Assuming you want to display the result in the specified result div
// //             let resultDiv = document.getElementById(resultDivId);

// //             // Format the result
// //             let formattedResult = `
// //                 Duration en minutes is: ${data.Duration_TSP_minutes}<br>
// //                 Route length in km: ${data.Route_Length}<br>
// //                 The clients: ${data.list_name_clients}<br>
// //                 To see the map click on:  <a href="${data.URL_html}" target="_blank">Maps</a>`;

// //             // Set the formatted result in the div
// //             resultDiv.innerHTML = formattedResult;
// //         })
// //         .catch(error => {
// //             console.error("Error", error);
// //         });
// //     }
// // });


// document.addEventListener("DOMContentLoaded", function() {
//     // Get both forms
//     let employeeForm = document.getElementById("employeeForm");
//     let employeeDateForm = document.getElementById("employeeDateForm");

//     // Add event listener to handle both form submissions
//     employeeForm.addEventListener("submit", function(event) {
//         event.preventDefault();
//         handleFormSubmission(employeeForm, "dates-result");
//     });

//     employeeDateForm.addEventListener("submit", function(event) {
//         event.preventDefault();
//         handleFormSubmission(employeeDateForm, "data-result");
//     });

//     function handleFormSubmission(form, resultDivId) {
//         fetch(form.getAttribute("action"), {
//             method: "POST",
//             body: new FormData(form),
//         })
//         .then(response => response.json())
//         .then(data => {
//             // Assuming you want to display the result in the specified result div
//             let resultDiv = document.getElementById(resultDivId);

//             // Format the result
//             let formattedResult = `
//                 Duration en minutes is: ${data.Duration_TSP_minutes}<br>
//                 Route length in km: ${data.Route_Length}<br>
//                 The clients: ${data.list_name_clients}<br>
//                 To see the map click on:  <a href="${data.URL_html}" target="_blank">Maps</a>`;

//             // Set the formatted result in the div
//             resultDiv.innerHTML = formattedResult;
//         })
//         .catch(error => {
//             console.error("Error", error);
//         });
//     }
// });
