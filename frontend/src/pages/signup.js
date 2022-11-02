import React from "react";
import styles from "./pages.css";
import { useLocation } from "react-router-dom";


const SignUp = () => {
  const location = useLocation();
  const { state } = location;
  console.log(state.props);

  return (
    <div className={styles.staticpage}>
      <h1>SignUp</h1>
    </div>
  );
};

export default SignUp;
