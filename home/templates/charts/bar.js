var ctx = document.getElementById("barChart").getContext("2d");
var labels = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Ago",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];
var barChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: labels,
    datasets: [
      {
        data: [69, 39, 69, 12, 49, 63, 24, 100, 69, 80, 30, 85],
        backgroundColor: ["rgba(1, 209, 255)"],
        borderColor: ["rgba(54, 162, 235, 0.2)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    plugins: {
      legend: {
        display: false,
      },
    },
    scales: {
      x: {
        ticks: {
          color: "#F3F4F6",
        },
      },
      y: {
        ticks: {
          color: "#F3F4F6",
        },
      },
    },
  },
});
