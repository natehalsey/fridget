import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Pages.css";
import axios from "axios";
import { API_URL, loginURL, signupURL } from "../constants";
import { AppContext } from "../constants";
import { useState } from "react";

const SignUp = () => {
    let navigate = useNavigate();
    const [error, setError] = useState(false);
    const [errorString, setErrorString] = useState();

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!e.target.email.value) {
            setError(true)
            setErrorString("Email is required.")
            return

        } else if (!e.target.username.value) {
            setError(true)
            setErrorString("Username required.")
            return
        } else if (!e.target.password.value) {
            setError(true)
            setErrorString("Password is required.")
            return
        }

        var bodyFormData = new FormData();
        bodyFormData.append('username', e.target.username.value);
        bodyFormData.append('password', e.target.password.value);
        bodyFormData.append('email', e.target.email.value)
        axios({
            method: "post",
            url: API_URL+signupURL,
            data: bodyFormData,
            headers: { "Content-Type": "multipart/form-data" },
        })
        .then( () => {
            setError(false)
            localStorage.setItem("auth", true)
            navigate("/home"); 
            
        })
        .catch( (error) => {
            localStorage.setItem("auth", false)
            setError(true)
            setErrorString(error.response?.data?.detail)
        });

    };
    

    return (
        <div className="LoginPage">
        <div className="LoginContainer">
        <form className="form" onSubmit={handleSubmit}>
            <div className="input-group">
            <label htmlFor="email">email</label>
            <input type="email" name="email" placeholder="email"/>
            </div>
            <div className="input-group">
            <label htmlFor="username">username</label>
            <input type="username" name="username" placeholder="username" />
            </div>
            <div className="input-group">
            <label htmlFor="password">Password</label>
            <input type="password" name="password" />
            </div>
            <button className="signupButton">Register</button>
        </form>
        {error &&
            <div className="errorString" color="red">
                {errorString}
            </div>
        }   
        </div>
         <a href="/home"></a>
        </div>
        
    );
}

export default SignUp;
