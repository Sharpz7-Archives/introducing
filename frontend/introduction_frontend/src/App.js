// import { useSelector } from 'react-redux';
// import Routes from 'routes/MainRoutes';
import IdentificationCard from 'views/pages/IdentificationCard';
import LandingPage from 'views/pages/LandingPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
// import { CssBaseline, StyledEngineProvider } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const baseTheme = createTheme();
// import themes from 'themes/mainTheme';

function App() {
    // const customization = useSelector((state) => state.customization);
    return (
        // <StyledEngineProvider injectFirst>
        //     <ThemeProvider>
        //         <CssBaseline />
        //         <Routes />
        //     </ThemeProvider>
        // </StyledEngineProvider>
        <ThemeProvider theme={baseTheme}>
            <Router>
                {/* <Header /> */}
                <Routes>
                    <Route exact path="/" element={<LandingPage />} />
                    <Route exact path="/dashboard" element={<LandingPage />} />
                    <Route path="/card-maker" element={<IdentificationCard />} />
                </Routes>
                {/* <Footer /> */}
            </Router>
        </ThemeProvider>
    );
}

export default App;
