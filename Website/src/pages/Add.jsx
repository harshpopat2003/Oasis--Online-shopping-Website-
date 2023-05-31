import axios from "axios";
import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Add = () => {

    const [user, setUser] = useState({
        First_Name:"",
        Middle_Name:"",
        Last_Name:"",
        Phone_Number:"",
        Email:"",
        Address:"",
        DOB:"",
    })

    const navigate = useNavigate()

    const handleChange = (e) =>{
        setUser(prev=>({ ...prev, [e.target.name]:e.target.value}))
    }

    const handleClick = async (e) =>{
        e.preventDefault()
        try{
            await axios.post("http://localhost:8000/users", user)
            navigate("/")
        }catch(err){
            console.log(err)
        }
    }

    console.log(user)

    return(
        <div className="form">
            <input type="text" placeholder = "First Name" onChange={handleChange} name="First_Name" style={{fontSize:20}}/>
            <input type="text" placeholder = "Middle Name" onChange={handleChange} name="Middle_Name" style={{fontSize:20}}/>
            <input type="text" placeholder = "Last Name" onChange={handleChange} name="Last_Name" style={{fontSize:20}}/>
            <input type="text" placeholder = "Phone Number" onChange={handleChange} name="Phone_Number" style={{fontSize:20}}/>
            <input type="text" placeholder = "Email" onChange={handleChange} name="Email" style={{fontSize:20}}/>
            <input type="text" placeholder = "Address" onChange={handleChange} name="Address" style={{fontSize:20}}/>
            <input type="text" placeholder = "DOB (YYYY-MM-DD)" onChange={handleChange} name="DOB" style={{fontSize:20}}/>

            <button onClick={handleClick} style={{fontSize:30}}>Add User</button>
        </div>
    )
}

export default Add