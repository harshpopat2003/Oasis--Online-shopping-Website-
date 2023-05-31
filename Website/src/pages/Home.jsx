import React from "react";
import { Link } from "react-router-dom";

const Home = () => {

    return(
        <div className="container">
            <h1 className="logo" style={{fontSize:50}}>OASIS</h1>
            <Link to="/users"><button style={{fontSize:30}}>List Users</button></Link>
            <Link to="/add"><button style={{fontSize:30}}>Add User</button></Link>
        </div>
    )
}

export default Home