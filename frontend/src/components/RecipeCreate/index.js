import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Toolbar from '@mui/material/Toolbar';
import Paper from '@mui/material/Paper';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Button from '@mui/material/Button';
//import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import IngredientsForm from './ingredients';
import Instructions from './instructions';
import Review from './review';
import axios from 'axios';
import { API_URL, createRecipeURL, loginURL } from "../../constants";
function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      
        Fridget
      {' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const steps = ['Enter Details', 'Enter Instructions', 'Review'];

  




const theme = createTheme();

export default function RecipeCreate() {


  const [activeStep, setActiveStep] = React.useState(0);
  const [recipe, setRecipe ] = React.useState({
    name: '',
    category: '',
    area: '',
    instructions: '',
    ingredients_measurements: [''],
    image_url: '',
    source: ''
  });
  const getStepContent = () => {
    switch (activeStep) {
      case 0:
        return <IngredientsForm recipe={recipe} change={setRecipe}/>;
      case 1:
        return <Instructions recipe={recipe} change={setRecipe}/>;
      case 2:
        return <Review recipe={recipe} change={setRecipe}/>;
      default:
        throw new Error('Unknown step');
    }
  }
  


   const handleNext = async () => {
    setActiveStep(activeStep + 1);
    if (activeStep===steps.length-1){
      
      axios.post(API_URL + createRecipeURL, { params: {
        name: recipe.name,
        ingredients_measurements:recipe.ingredients_measurements,
        area: recipe.area,
        category: recipe.category,
        instructions: recipe.instructions
      }}).then((response) =>{
          console.log(response.response.data);
      }).catch(err =>{
        console.log(err.response.data);
      });
      console.log(recipe)
    }
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };




  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppBar
        position="absolute"
        color="default"
        elevation={0}
        sx={{
          position: 'relative',
          borderBottom: (t) => `1px solid ${t.palette.divider}`,
        }}
      >
        

        <Toolbar>
          <Typography variant="h6" color="inherit" noWrap>
            Fridget Recipe Creation
          </Typography>
        </Toolbar>
      </AppBar>


      <Container component="main" maxWidth="sm" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
          <Typography component="h1" variant="h4" align="center">
            Create Your Recipe
          </Typography>
          <Stepper activeStep={activeStep} sx={{ pt: 3, pb: 5 }}>
            {steps.map((label) => (
              <Step key={label}>
                <StepLabel>{label}</StepLabel>
              </Step>
            ))}
          </Stepper>


          {activeStep === steps.length ? (         
            <React.Fragment>
              <Typography variant="h5" gutterBottom>
               Your Recipe Has Been Submitted. <br />
               Thank You.
              </Typography>              
            </React.Fragment>
          ) : (
            <React.Fragment>
              {getStepContent(activeStep)}
              <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                {activeStep !== 0 && (
                  <Button onClick={handleBack} sx={{ mt: 3, ml: 1 }}>
                    Back
                  </Button>
                )}



                <Button
                  variant="contained"
                  onClick={handleNext}
                  sx={{ mt: 3, ml: 1 }}
                >
                  {activeStep === steps.length - 1 ? 'Submit' : 'Next'}
                </Button>
              </Box>
            </React.Fragment>
          )}
        </Paper>
        <Copyright />
      </Container>
    </ThemeProvider>
  );
}

