import React, { useEffect, useState } from "react";
import styles from "./SearchBar.css";
import axios from "axios";

const SearchBar = () => {
  const [query, setQuery] = useState([]);
  const [searchTitle, setSearchTitle] = useState("");

  useEffect(() => {
    const loadQuery = async () => {
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/posts"
      );
      setQuery(response.data);
    };

    loadQuery();
  }, []);

  return (
    <div className={styles.staticpage}>
      <h1>Welcome to App!</h1>
      <input
        type="text"
        placeholder="Search..."
        className="search"
        onChange={(e) => setSearchTitle(e.target.value)}
      />
      <ul className="list">
        {query
          .filter((value) => {
            if (searchTitle === "") {
              return value;
            } else if (
              value.title.toLowerCase().includes(searchTitle.toLowerCase())
            ) {
              return value;
            }
          })
          .map((item) => (
            <li key={item.id} className="listItem">
              {item.title}
            </li>
          ))}
      </ul>
    </div>
  );
};

export default SearchBar;
