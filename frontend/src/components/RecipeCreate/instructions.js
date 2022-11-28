import * as React from 'react';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
//import FormControlLabel from '@mui/material/FormControlLabel';
//import Checkbox from '@mui/material/Checkbox';

export default function Instructions({recipe, change}) {
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
            onChange={(e)=>{
              change({...recipe, instructions: e.target.value})
            }}
            multiline
            minRows={6}
            variant="filled"
          />
      </Grid>
    </React.Fragment>
  );
}

