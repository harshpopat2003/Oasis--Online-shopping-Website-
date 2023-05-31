import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom"; 
import Add from "./pages/Add";
import Home from "./pages/Home";
import Users from "./pages/Users";
import "./style.css"


function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element = {<Home/>}/>
        <Route path="/add" element = {<Add/>}/>
        <Route path="/users" element = {<Users/>}/>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
