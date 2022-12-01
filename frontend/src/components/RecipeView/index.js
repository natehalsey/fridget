import React from "react";
import Typography from "@mui/material/Typography";
import axios from "axios";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import { API_URL, getRecipeByIdURL, AppContext, routes } from "../../constants";
import Table from "../IngredientsTable";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";
import FavoriteIcon from "@mui/icons-material/Favorite";
import IconButton from "@mui/material/IconButton";
import "./styles.css";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

/**
 * This function is responsible for displaying the recipe details page
 * @returns The RecipeView component
 */
export default function RecipeView() {
  const path = window.location.pathname.split("/");
  const [recipeData, setRecipeData] = React.useState();
  const [saved, setSaved] = React.useState();
  const [created, setCreated] = React.useState();
  const id = path[path.length - 1];
  const navigate = useNavigate();

  React.useEffect(() => {
    getRecipe(id);
    getSavedRecipes();
  }, [localStorage.getItem("auth")]);

  React.useEffect(() => {
    getCreatedRecipes();
  }, [localStorage.getItem("auth")]);

  const getRecipe = (id) => {
    axios
      .get(API_URL + getRecipeByIdURL, { params: { id: id } })
      .then((response) => {
        setRecipeData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const handleDelete = () => {
    // eslint-disable-next-line no-restricted-globals
    const confirm_delete = confirm(
      "Are you sure you want to delete " + recipeData?.name + "?"
    );
    if (confirm_delete) {
      removeCreatedRecipe();
      navigate(routes.home);
    }
  };

  const onSave = () => {
    if (saved) {
      setSaved(false);
      removeSavedRecipe();
    } else {
      setSaved(true);
      saveRecipe();
    }
  };

  const getCreatedRecipes = () => {
    axios({
      method: "get",
      url: API_URL + "/users/get-created-recipes",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => {
        response.data.find((recipe) => recipe.id == id)
          ? setCreated(true)
          : setCreated(false);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const getSavedRecipes = () => {
    axios({
      method: "get",
      url: API_URL + "/users/get-saved-recipes",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => {
        response.data.find((recipe) => recipe?.id == id)
          ? setSaved(true)
          : setSaved(false);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const saveRecipe = () => {
    axios({
      method: "post",
      url: API_URL + `/users/save-recipe?id=${id}`,
      headers: { "Content-Type": "application/json" },
    }).catch((error) => {
      console.log(error);
      localStorage.setItem("auth", false);
    });
  };

  const removeSavedRecipe = () => {
    axios({
      method: "delete",
      url: API_URL + `/users/remove-saved-recipe?id=${id}`,
      headers: { "Content-Type": "application/json" },
    })
      .then(() => {
        setSaved(false);
      })
      .catch((error) => {
        console.log(error);
        localStorage.setItem("auth", false);
      });
  };
  const removeCreatedRecipe = () => {
    axios({
      method: "delete",
      url: API_URL + `/users/remove-created-recipe?id=${id}`,
      headers: { "Content-Type": "application/json" },
    }).catch((error) => {
      console.log(error);
      localStorage.setItem("auth", false);
    });
  };

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
              <Grid item xs={12} sm={12} md={12} lg={12}>
                <Card>
                  <CardContent>
                    <div className="recipe-header">
                      <Typography gutterBottom variant="h5" component="div">
                        {recipeData?.name}
                      </Typography>

                      {localStorage.getItem("auth") === "true" && (
                        <IconButton className="heart" onClick={onSave}>
                          {saved ? <FavoriteIcon /> : <FavoriteBorderIcon />}
                        </IconButton>
                      )}
                      {created && (
                        <Button onClick={handleDelete}>Delete Recipe</Button>
                      )}
                    </div>
                    <Typography variant="body2" color="text.secondary">
                      Category: {recipeData?.category?.name} | Cuisine:{" "}
                      {recipeData?.area?.name}
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
              <Typography color="text.primary">
                <pre className="instructions">{recipeData?.instructions}</pre>
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Stack>
    </div>
  );
}
