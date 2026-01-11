import { useEffect, useState } from "react"
import axios from "axios"

function App() {
  const [status, setStatus] = useState("Checking backend...")

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/health")
      .then(res => setStatus(res.data.message))
      .catch(() => setStatus("Backend not reachable"))
  }, [])

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <h1 className="text-xl font-semibold">
        {status}
      </h1>
    </div>
  )
}

export default App
