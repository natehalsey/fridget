import React, { useCallback } from "react";
import { useEffect, useContext } from "react";
import jwt_decode from "jwt-decode";
import { AppContext } from "../../constants"
import axios from "axios";
import * as Constants from "../../constants"
import ResponsiveAppBar from "./AppBar"

const Navbar = () => {
  const {user, setUser} = useContext(AppContext);

  function handleSignOut(event) {
    setUser({});
    document.getElementById("signInDiv").hidden = false;
  }
  
  const sendUserFormData = ( (data) => {
    axios.post(Constants.API_URL+Constants.postUserData, data)
      .then( ({ data }) => {
        setUser({...user, data });
      })
      .catch( (error) => {
        console.log(error);
      });
    
      console.log(user);
  })

  const handleCallbackResponse = useCallback((response) => {
    var userObject = jwt_decode(response.credential);

    setUser({...user, ...userObject});
    var data = {
      "given_name": userObject.given_name,
      "family_name": userObject.family_name,
      "picture": userObject.picture,
      "email": userObject.email
    };
    //sendUserFormData(data); TODO uncomment when BE auth is ready
    document.getElementById("signInDiv").hidden = true;
  }, []);

  useEffect(() => {
    /* global google */
    try {
    google?.accounts.id.initialize({
      client_id:
        "982127523493-8rbf1c72sp24kadsbm7ku62feja2scqj.apps.googleusercontent.com",
      callback: handleCallbackResponse,
    });

    google?.accounts.id.renderButton(document.getElementById("signInDiv"), {
      theme: "Outline",
      size: "large",
    });
  } catch (e) {
    console.log("Google Auth Failed");
  }
  }, [handleCallbackResponse]);

  return (
    <ResponsiveAppBar></ResponsiveAppBar>
  );
};

export default Navbar;
