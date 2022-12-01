import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";

/**
 * It's a function that takes in a recipe object and a change function, and returns a React Fragment
 * that contains a Typography component and a Grid component that contains a TextField component
 * @returns The Instructions step component is being returned.
 */
export default function Instructions({ recipe, change }) {
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
        Recipe Instructions:
      </Typography>
      <Grid item xs={12}>
        <TextField
          required
          id="instructions"
          name="instructions"
          label="Enter Instructions"
          fullWidth
          value={recipe.instructions}
          onChange={(e) => {
            change({ ...recipe, instructions: e.target.value });
          }}
          multiline
          minRows={6}
          variant="filled"
        />
      </Grid>
    </React.Fragment>
  );
}
