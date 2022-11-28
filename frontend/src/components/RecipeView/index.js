import React from "react";
import Typography from '@mui/material/Typography';
import axios from "axios";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { API_URL, getRecipeByIdURL, AppContext } from "../../constants";
import Table from '../IngredientsTable';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import FavoriteIcon from '@mui/icons-material/Favorite';
import IconButton from '@mui/material/IconButton';
import styles from "./styles.css";

export default function RecipeView() {
    const path = window.location.pathname.split('/');
    const [recipeData, setRecipeData] = React.useState();
    const { auth } = React.useContext(AppContext);
    const [saved, setSaved] = React.useState();

    React.useEffect(() => {
        var id = path[path.length - 1];
        getRecipe(id);
        if (auth) {
            const saved_recipes = getSavedRecipes();
            saved_recipes.find((recipe) => recipe?.id === id) ? setSaved(true) : setSaved(false);
        }
    },[auth]);

    const onSave = () => {
        setSaved(true);
        saveRecipe();
    };

    const getSavedRecipes = () => { 
        axios({
            method: "get",
            url: API_URL + "/users/get-created-recipes",
            headers: {"Content-Type": 'application/json'},
        }).then( (response) => {
            return response.data;
        })
        .catch( (error) => {
            console.log(error);
            return [];
        });
    };

    const saveRecipe = () => {
        var bodyFormData = new FormData();
        bodyFormData.append('id',  path[path.length - 1]);
        axios({
            method: "post",
            url: API_URL + "/users/save-recipe",
            data: bodyFormData,
            headers: { "Content-Type": "multipart/form-data" },
        })
        .then( (response) => {
            console.log(response.status)
            
        })
        .catch( (error) => {
            console.log(error)
        });
    };

    const getRecipe = ( (id) => {
        axios.get(
            API_URL + getRecipeByIdURL, { params: { id: id }}
        ).then( (response) => {
            setRecipeData(response.data)
        })
        .catch( (error) => {
            console.log(error);
        });
    });

    return (
        <div className="recipe-view">
            <Stack container>
                <Grid container spacing={1}>

                    <Grid item xs={12} sm={12} md={4} lg={4}>
                        <Card>
                            <CardMedia
                                component="img"
                                alt="green iguana"
                                height="500"
                                image={recipeData?.image_url}
                            />
                        </Card>
                    </Grid>

                    <Grid item xs={12} sm={12} md={8} lg={8}>
                        <Grid container>
                            <Grid item xs={12} sm={12}md={12} lg={12}>
                                <Card>
                                    <CardContent>
                                        <div className="recipe-header">
                                            <Typography gutterBottom variant="h5" component="div">
                                                {recipeData?.name}
                                            </Typography>
                                            
                                            {
                                                auth && <IconButton className="heart" onClick={onSave}>
                                                   { saved ? <FavoriteIcon /> : <FavoriteBorderIcon /> }
                                                </IconButton>
                                            }
                                        </div>
                                        <Typography variant="body2" color="text.secondary">
                                            Category: {recipeData?.category?.name} | Cuisine: {recipeData?.area?.name}
                                        </Typography>
                                        <Table rows={recipeData?.ingredients_measurements} />
                                    </CardContent>
                                </Card>
                            </Grid>
                        </Grid>                    
                    </Grid>
                </Grid>
                <Grid spacing={2}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" color="text.primary">
                                {recipeData?.instructions}
                            </Typography>
                        </CardContent>
                    </Card>
                </Grid>
            </Stack>
        </div>
    );

    /* return (

        <Card raised>
            <CardMedia
                component="img"
                alt="green iguana"
                height="200"
                image={recipeData?.image_url}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {recipeData?.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Category: {recipeData?.category?.name} | Cuisine: {recipeData?.area?.name}
                </Typography>
                <Table rows={recipeData?.ingredients_measurements} />
                
                <Divider />
                
                <Paper>
                    <Typography variant="body1" color="text.primary">
                        {recipeData?.instructions}
                    </Typography>
                </Paper>
            </CardContent>
        </Card>
    ); */
}