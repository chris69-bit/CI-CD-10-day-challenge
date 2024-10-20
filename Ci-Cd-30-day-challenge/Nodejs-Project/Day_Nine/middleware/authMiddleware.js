// Example of a simple authentication middleware
module.exports = (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (!authHeader || authHeader !== 'Bearer mysecrettoken') {
        return res.status(403).json({ message: 'Forbidden' });
    }
    next();
};
