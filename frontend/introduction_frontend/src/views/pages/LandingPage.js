import { Grid, Typography, useMediaQuery, Button, Stack } from '@mui/material';
import { useTheme } from '@mui/material/styles';

function LandingPage() {
    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('md'));

    return (
        <Stack textAlign={isMobile ? 'center' : ''}>
            <Grid container display="flex" minHeight="100vh" textAlign={isMobile ? 'center' : ''} minWidth="100vw">
                <Grid item lg={6} xl={6} sm={6} xs={6} backgroundColor="black">
                    <Grid container mt={isMobile ? '150%' : '5%'}>
                        <Grid item lg={12} xl={12} sm={12} xs={12}>
                            <Typography
                                fontSize={isMobile ? '400%' : '200px'}
                                textAlign="right"
                                sx={{ fontFamily: 'Smooch, cursive' }}
                                fontStyle=""
                                color="white"
                                fontWeight="700px"
                            >
                                Introd <br /> <span>Card</span>
                            </Typography>
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item lg={6} xl={6} sm={6} xs={6} backgroundColor="white">
                    <Grid container direction="column" mt={isMobile ? '150%' : '5%'}>
                        <Grid item lg={12} xl={12} sm={12} xs={12}>
                            <Typography
                                fontSize={isMobile ? '400%' : '200px'}
                                textAlign="left"
                                sx={{ fontFamily: 'Smooch, cursive' }}
                                fontStyle=""
                                color="#000"
                                fontWeight="700px"
                            >
                                ucing <br />
                                <span>Maker</span>
                            </Typography>
                            <Button
                                variant="contained"
                                sx={{
                                    backgroundColor: '#000',
                                    fontFamily: 'Smooch, cursive',
                                    color: '#fff',
                                    textTransform: 'none',
                                    '&:hover': { backgroundColor: 'DimGrey' }
                                }}
                                disableElevation
                                href="/card-maker"
                            >
                                Create Card
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </Stack>
    );
}

export default LandingPage;
