import React from "react";
import MenuTray from "../components/MenuTray";
import Search from "../components/Search";

/**
 * The Home component returns the Search component
 * @returns A React component
 */
const Home = () => {
  return (
    <div className="home">
      <Search />
    </div>
  );
};

export default Home;
