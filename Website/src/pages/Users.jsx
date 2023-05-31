import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import axios from "axios";

const Users = () => {
    const [users, setUsers] = useState([])

    useEffect(() => {
        const fetchAllUsers = async ()=>{
            try{
                const res = await axios.get("http://localhost:8000/users")
                setUsers(res.data)
            }catch(err){
                console.log(err)
            }
        }
        fetchAllUsers()
    },[])

    return(
        <div className="containerUsers">
            <h1 className="logo">OASIS</h1>
            <div className="users">
                {users.map(user=>(
                    <div className="user" key={user.Customer_ID}>
                        <p className="userItem">{user.First_Name}</p>
                        <p className="userItem">{user.Middle_Name}</p>
                        <p className="userItem">{user.Last_Name}</p>
                        <p className="userItem">{user.Phone_Number}</p>
                        <p className="userItem">{user.Email}</p>
                        <p className="userItem">{user.Address}</p>
                        <p className="userItem">{user.DOB}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Users