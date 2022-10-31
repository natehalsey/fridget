import React from 'react';
import styles from "./pages.css";
import Search from '../components/Search';
const SearchPage = () => {
  return (
    <div className={styles.staticpage}>
      <Search/>
    </div>
  );
};
  
export default SearchPage;