// const accessToken = "643e282d90ce2a7c5a6b0c6387837cd0d4609053";

// fetch("https://www.strava.com/api/v3/athlete/activities", {
//   headers: {
//     Authorization: "Bearer " + accessToken
//   }
// })
// .then(res => res.json())
// .then(data => console.log(data))
// .catch(err => console.error("Error:", err));

const accessToken = "643e282d90ce2a7c5a6b0c6387837cd0d4609053";

fetch("https://www.strava.com/api/v3/athlete/activities", {
    headers: {
      Authorization: "Bearer " + accessToken
    }
  })
    .then(res => res.json())  // ✅ parse the response body
    .then(data => {
      const output = document.getElementById("strava-output");
      output.innerHTML = ""; // Clear "Loading..."
  
      data.slice(0, 10).forEach(activity => {
        const card = document.createElement("div");
        card.className = "strava-card";
  
        card.innerHTML = `
  <h3><a href="https://www.strava.com/activities/${activity.id}" target="_blank" rel="noopener noreferrer">${activity.name}</a></h3>
  <p><strong>Distance:</strong> ${(activity.distance / 1000).toFixed(2)} km</p>
  <p><strong>Type:</strong> ${activity.type}</p>
  <p><strong>Date:</strong> ${new Date(activity.start_date).toLocaleDateString()}</p>
  <p><strong>Time:</strong> ${Math.round(activity.moving_time / 60)} minutes</p>
`;

  
        output.appendChild(card);
      });
    })
    .catch(err => console.error("Error:", err));
  
