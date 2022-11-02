import React, { useCallback } from "react";
import { Nav, NavLink, Bars, NavMenu, NavBtn } from "./NavbarElements";
import { useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

const Navbar = () => {
  const [user, setUser] = useState({});

  const handleCallbackResponse = useCallback((response) => {
    var userObject = jwt_decode(response.credential);
    setUser(userObject);
  });

  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id:
        "982127523493-8rbf1c72sp24kadsbm7ku62feja2scqj.apps.googleusercontent.com",
      callback: handleCallbackResponse,
    });

    google.accounts.id.renderButton(document.getElementById("signInDiv"), {
      theme: "Outline",
      size: "large",
    });
  }, [handleCallbackResponse]);

  // If we have no user, show sign in button

  // If we have user, show log out button

  return (
    <div>
      <Nav>
        <Bars />

        <NavMenu>
          <NavLink to="/about" activeStyle>
            About
          </NavLink>
          <NavLink to="/team" activeStyle>
            Team
          </NavLink>
          <NavLink to="/api" activeStyle>
            API
          </NavLink>
        </NavMenu>
        <NavLink to="/signup" state={{ props: user }}>
          <NavBtn>
            <div id="signInDiv" to="/signin" />
          </NavBtn>
        </NavLink>
      </Nav>
    </div>
  );
};

export default Navbar;
