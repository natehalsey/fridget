import React from "react";
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import axios from "axios";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { baseURL, getRecipeByIdURL } from "../../constants";
import Table from '../IngredientsTable';
import Divider from '@mui/material/Divider';

export default function RecipeView() {
    const path = window.location.pathname.split('/');
    const [recipeData, setRecipeData] = React.useState();

    const getRecipe = async () => {
        const id = path[path.length - 1]

        return await axios.get(
            baseURL + getRecipeByIdURL, { params: { id: id }}
            );
    };

    React.useEffect(() => {
        getRecipe().then(res => setRecipeData(res?.data));
    });

    return (
        <Card raised>
            <CardMedia
                component="img"
                alt="green iguana"
                height="200"
                image={recipeData?.image_url}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    Name: {recipeData?.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Category: {recipeData?.category?.name} | Area: {recipeData?.area?.name}
                </Typography>
                <Table rows={recipeData?.ingredients_measurements} />
                
                <Divider />
                
                <Paper>
                    <Typography variant="body1" color="text.primary">
                        Instructions: {recipeData?.instructions}
                    </Typography>
                </Paper>
            </CardContent>
        </Card>
    );
}