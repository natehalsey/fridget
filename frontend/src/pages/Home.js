import React from "react";
import SearchBar from "../components/SearchBar/SearchBar";
import styles from "./pages.css";

const Home = () => {
  return (
    <div className={styles.staticpage}>
      <SearchBar></SearchBar>
    </div>
  );
};

export default Home;
