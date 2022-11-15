import React from "react";
import Grid from '@mui/material/Grid';
import Search from "../components/Search";
import SideMenu from "../components/SideMenu";

const Home = () => {
  return (
    <div className="home">
      <Grid container spacing={2}>
        <Grid item xs={2}>
          <SideMenu/>
        </Grid>
        <Grid item xs={9}>
          <Search />
        </Grid>
      </Grid>
    </div>
  );
};

export default Home;
