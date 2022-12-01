import * as React from 'react';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Input from '@mui/material/Input';
import AddIcon from '@mui/icons-material/Add';
import IconButton from '@mui/material/IconButton';
import TableFooter from '@mui/material/TableFooter';

export default function IngredientsForm({recipe, change}) {
  const [ingredient, setIngredient] = React.useState();
  const [measurement, setMeasurement] = React.useState();

  console.log(recipe.ingredients_measurements);

  const addIngredient = () => {
    console.log(ingredient, measurement);
    if (ingredient && measurement) {
      change({
        ...recipe,
        ...recipe.ingredients_measurements.push({
            ingredient: ingredient,
            measurement: measurement,
          })
      });
    }
    console.log(recipe);
    setIngredient();
    setMeasurement();
  }


  return (
    <>
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
            label="Cusisine"
            fullWidth
            value={recipe.area}
            onChange={(e)=>{
              change({...recipe, area: e.target.value})
            }}
            variant="standard"
          />
       
        </Grid>
        
        
        
       
        <Grid item xs={12}>
        <TableContainer component={Paper} size="small">
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Ingredient</TableCell>
                <TableCell align="right">Measurement</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
                {recipe.ingredients_measurements?.map(({ingredient, measurement}, index) => (
                  <TableRow>
                    <TableCell>{ingredient}</TableCell>
                    <TableCell align="right">{measurement}</TableCell>
                  </TableRow>
                ))}
            </TableBody>

            <TableFooter>
              <TableRow xs={2} sm={2} md={12} lg={12}>
                <TableCell xs={2} sm={2} md={12} lg={12}>
                  <TextField
                    className="ingredient"
                    id="Ingredient"
                    label="Ingredient"
                    name="Ingredient"
                    value={ingredient}
                    fullWidth
                    variant="standard"
                    onChange={(e) => setIngredient(e.target.value)} 
                  />
                </TableCell>
                <TableCell xs={2} sm={2} md={12} lg={12}>
                  <TextField
                      className="measurement"
                      id="Measurement"
                      label="Measurement"
                      name="Measurement"
                      value={measurement}
                      fullWidth
                      variant="standard"
                      onChange={(e) => setMeasurement(e.target.value)} 
                    />
                </TableCell>
                <TableCell align="right" xs={2} sm={2} md={12} lg={12}>
                  <IconButton onClick={addIngredient}>
                    <AddIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            </TableFooter>
          </Table>  
          </TableContainer>
        </Grid>
      </Grid>
    </>
  );
}

