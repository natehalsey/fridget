import React from "react";
import Grid from '@mui/material/Grid';
import SearchBar from "../components/SearchBar/SearchBar";
import SideMenu from "../components/SideMenu/SideMenu";

const Home = () => {
  // TODO: useCOnext get serach parms from side menu
  return (
    <div className="home">
      <Grid container spacing={2}>
        <Grid item xs={2}>
          <SideMenu/>
        </Grid>
        <Grid item xs={9}>
          <SearchBar />
        </Grid>
      </Grid>
    </div>
  );
};

export default Home;
