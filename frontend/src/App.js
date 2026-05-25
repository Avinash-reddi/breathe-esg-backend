import './App.css';

function App() {
  const companies = [
    {
      name: "Tesla",
      industry: "Automotive",
      esg: -145.5
    },
    {
      name: "Infosys",
      industry: "IT",
      esg: 13.0
    },
    {
      name: "TCS",
      industry: "IT",
      esg: -12.5
    },
    {
      name: "Wipro",
      industry: "IT",
      esg: 24.5
    }
  ];

  return (
    <div className="container">
      <h1>Breathe ESG Dashboard</h1>

      <table>
        <thead>
          <tr>
            <th>Company</th>
            <th>Industry</th>
            <th>ESG Score</th>
          </tr>
        </thead>

        <tbody>
          {companies.map((company, index) => (
            <tr key={index}>
              <td>{company.name}</td>
              <td>{company.industry}</td>
              <td>{company.esg}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;