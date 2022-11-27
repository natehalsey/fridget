import React from "react";
import Grid from '@mui/material/Grid';
import Search from "../components/Search";
import SideMenu from "../components/SideMenu";
import DesktopBreakpoint from "../components/Breakpoint/desktop"
import PhoneBreakpoint from "../components/Breakpoint/phone"
const Home = () => {
  return (
    <div className="home">
      <h1>TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT</h1>
      <DesktopBreakpoint>
        <Grid container spacing={2}>
          <Grid item xs={2}>
            <SideMenu/>
          </Grid>
          <Grid item xs={9}>
            <Search />
          </Grid>
        </Grid>
      </DesktopBreakpoint>

      <PhoneBreakpoint>
        <h1>poooo!</h1>
      </PhoneBreakpoint>
    </div>
  );
};

export default Home;
