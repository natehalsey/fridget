import { Accordion, Button, Typography } from "@mui/material";
import React from "react";
import UserSavedRecipes from "../components/UserSavedRecipes";
import UserCreatedRecipes from "../components/UserCreatedRecipes";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const MyRecipes = () => {
  return (
    <div className="MyRecipesPage">
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography variant="h5">Saved Recipes</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <UserSavedRecipes />
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography variant="h5">Created Recipes</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <UserCreatedRecipes />
        </AccordionDetails>
      </Accordion>
    </div>
  );
};
export default MyRecipes;
