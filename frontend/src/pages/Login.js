import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Pages.css";
import axios from "axios";
import { API_URL, loginURL } from "../constants";
import { AppContext } from "../constants";
import { useState } from "react";

/**
 * Returns a div with the login form that submits to the backend and navigates to the home page on successfull login
 * @returns A React component
 */
const Login = () => {
  let navigate = useNavigate();
  const [error, setError] = useState(false);
  const [errorString, setErrorString] = useState();
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!e.target.username.value) {
      setError(true);
      setErrorString("Username required.");
      return;
    } else if (!e.target.password.value) {
      setError(true);
      setErrorString("Password is required.");
      return;
    }

    if (e.nativeEvent.submitter.className === "loginButton") {
      console.log("sign up");
    } else {
      console.log("log in");
    }

    var bodyFormData = new FormData();
    bodyFormData.append("username", e.target.username.value);
    bodyFormData.append("password", e.target.password.value);
    axios({
      method: "post",
      url: API_URL + loginURL,
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then((response) => {
        localStorage.setItem("auth", true);
        navigate("/home");
      })
      .catch((error) => {
        console.log(error);
        localStorage.setItem("auth", false);
      });
  };

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
          <button className="loginButton">Login</button>
        </form>
        Don't have an account? <a href="/signup"> Register</a>
        {error && (
          <div className="errorString" color="red">
            {errorString}
          </div>
        )}
      </div>
      <a href="/home"></a>
    </div>
  );
};

export default Login;
