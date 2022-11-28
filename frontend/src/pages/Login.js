import React, { useEffect } from "react";
import "./Pages.css";
import axios from "axios";
import { API_URL, loginURL } from "../constants";
import { AppContext } from "../constants";

const Login = () => {
    const {auth, setAuth} = React.useContext(AppContext);
    console.log(auth+" a")
    const handleSubmit = (e) => {
        e.preventDefault();

        if (!e.target.username.value) {
            alert("username required");
            return

        } else if (!e.target.password.value) {
            alert("Password is required");
            return
        }

        var bodyFormData = new FormData();
        bodyFormData.append('username', e.target.username.value);
        bodyFormData.append('password', e.target.password.value);
        axios({
            method: "post",
            url: API_URL+loginURL,
            data: bodyFormData,
            headers: { "Content-Type": "multipart/form-data" },
        })
        .then( (response) => {
            console.log(response.status)
        })
        .catch( (error) => {
            console.log(error)
        });

    };
    useEffect(() => {
        setAuth(true)
    },[handleSubmit])

    return (
        <div className="LoginPage">
        <div className="LoginContainer">
        <form className="form" onSubmit={handleSubmit}>
            <div className="input-group">
            <label htmlFor="username">username</label>
            <input type="username" name="username" placeholder="username" />
            </div>
            <div className="input-group">
            <label htmlFor="password">Password</label>
            <input type="password" name="password" />
            </div>
            <button className="loginButtonPrimary">Login</button>
        </form>
        </div>
        </div>
    );
}

export default Login;