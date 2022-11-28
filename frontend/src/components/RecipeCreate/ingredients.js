import * as React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
//import FormControlLabel from '@mui/material/FormControlLabel';
//import Checkbox from '@mui/material/Checkbox';

export default function IngredientsForm({recipe, change}) {
  return (
    <React.Fragment>
      <Typography variant="h6" gutterBottom>
        Your Recipe Info
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="name"
            name="name"
            label="Name"
            fullWidth
            value={recipe.name}
            onChange={(e)=>{
              change({...recipe, name: e.target.value})
            }}
            variant="standard"
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            id="category"
            name="category"
            label="Category"
            fullWidth
            variant="standard"
            value={recipe.category}
            onChange={(e) => {
              change({...recipe, category: e.target.value})
            }}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            id="area"
            name="area"
            label="Recipe Area"
            fullWidth
            value={recipe.area}
            onChange={(e)=>{
              change({...recipe, area: e.target.value})
            }}
            variant="standard"
          />
       
        </Grid>
        
        
        
       
        <Grid item xs={12}>
          <TextField
            required
            id="ingredients"
            name="ingredients"
            label="Ingredients (enter ingredients seperated by a , )"
            fullWidth
            multiline
            value={recipe.ingredients_measurements}
            onChange={(e)=>{
              change({...recipe, ingredients_measurements: e.target.value.split(",")})
            }}
            minRows={4}
            variant="filled"
          />
        </Grid>
      </Grid>
    </React.Fragment>
  );
}

