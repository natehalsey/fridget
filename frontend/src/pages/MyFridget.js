import React from 'react';
import { Grid, Button } from '@mui/material';
import axios from "axios";
import { useNavigate } from "react-router-dom";
import RecipeCard from '../components/RecipeCard';
import FridgetListItem from "../components/FridgetListItem"
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { 
    searchParamIngredient,
    getRecipeByIngredientURL,
    AppContext, 
    API_URL, 
  } from "../constants";

const MyFridget = () => {
    const [searchResults, setSearchResults] = React.useState();
    const { checked } = React.useContext(AppContext);
    const navigate = useNavigate();
    const loadQuery = async (url, params) => {
        return await axios.get(url, {params});
      };
    const getRecipesByFridget = () => {
        loadQuery(API_URL +   getRecipeByIngredientURL, {[searchParamIngredient]: checked.join()}
        ).then( (response) => {
            setSearchResults(response.data)
        }).catch( (error) => {
                console.log(error);
                localStorage.setItem("auth", false)
                navigate("/home")
            });
    };

    React.useEffect(() => {
        getRecipesByFridget();
    }, [checked])

    return (
        <div>
            <Accordion>
                <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                >
                <Typography variant="h5">Whats in my Fridget?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <FridgetListItem></FridgetListItem>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                >
                <Typography variant="h5">Whats can I make?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Grid container spacing={1}>
                        {searchResults?.map((row) => (
                            <Grid key={row?.id} item xs={12} sm={4} md={3} lg={3}>
                                <RecipeCard data={row} className="list"></RecipeCard>
                            </Grid>
                        ))}
                    </Grid>
                </AccordionDetails>
            </Accordion>
        </div>        
    )
}

export default MyFridget;