import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";

/**
 * The Review function is a React component that allows the user to review their recipe before saving
 * @returns The Review component
 */
export default function Review({ recipe, change }) {
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
        Recipe summary
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <Typography variant="h6" gutterBottom sx={{ mt: 2 }}>
            Recipe Info
          </Typography>
          <Typography gutterBottom>Name: {recipe.name}</Typography>
          <Typography gutterBottom>Area: {recipe.area}</Typography>
          <Typography gutterBottom>Category: {recipe.category}</Typography>
        </Grid>
        <Grid item container direction="column" xs={12} sm={6}>
          <Typography variant="h6" gutterBottom sx={{ mt: 2 }}>
            Ingredients
          </Typography>
          <Grid container>
            {recipe.ingredients_measurements.map(
              ({ ingredient, measurement }) => (
                <Grid item key={ingredient} xs={6}>
                  <Typography gutterBottom key={ingredient}>
                    {ingredient}
                  </Typography>
                </Grid>
              )
            )}
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
}
