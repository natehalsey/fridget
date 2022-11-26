const defaultSettings = {
  REACT_APP_API_URL: 'http://localhost:8000',
};
const settings = {defaultSettings, ...process.env};
export default settings;