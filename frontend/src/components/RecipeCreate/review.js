import * as React from 'react';
import Typography from '@mui/material/Typography';
/**import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
**/
import Grid from '@mui/material/Grid';





export default function Review({recipe, change}) {
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
            {recipe.ingredients_measurements.map((ing) => (
                <Grid item key={ing} xs={6}>
                  <Typography gutterBottom key={ing}>{ing}</Typography>
                </Grid>

            ))}
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
}

