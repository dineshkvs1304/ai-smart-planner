import { useState } from "react";

function App() {
  const [tasks, setTasks] = useState("");
  const [schedule, setSchedule] = useState([]);

  const generatePlan = async () => {
    const taskList = tasks.split(",");

    const res = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ tasks: taskList }),
    });

    const data = await res.json();
    setSchedule(data.schedule);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Smart Daily Planner</h1>

      <p>Enter tasks separated by comma:</p>

      <input
        style={{ width: "400px", padding: "10px" }}
        value={tasks}
        onChange={(e) => setTasks(e.target.value)}
        placeholder="DSA study, Gym, Project, Netflix"
      />

      <br /><br />

      <button
        onClick={generatePlan}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          background: "black",
          color: "white",
          border: "none",
        }}
      >
        Generate Smart Schedule
      </button>

      <h2>Today's Plan:</h2>

      {schedule.map((item, index) => (
        <div key={index}>
          {item.time} → {item.task}
        </div>
      ))}
    </div>
  );
}

export default App;