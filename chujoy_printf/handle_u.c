/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_u.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 18:10:16 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/11 18:10:17 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_u(va_list *arg)
{
	unsigned int	val;
	int				count;

	val = va_arg(*arg, unsigned int);
	count = ft_putnbr_unsigned(val);
	return (count);
}
